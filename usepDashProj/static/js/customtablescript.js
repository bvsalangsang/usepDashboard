const csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;

var tempData;
var lvl2Data;

function findNestedObj(entireObj, keyToFind, valToFind) {
	let foundObjs;

	JSON.stringify(entireObj, (_, nestedValue) => {
		if (nestedValue && nestedValue[keyToFind] === valToFind) {
			foundObjs = nestedValue;
		}
		return nestedValue;
	});
	return foundObjs;
}

function createChild(row, rowData, keyName, rowId, level) {
	var numLevels = 2; // Number of child levels with .details-control
	var trData;

	// This is the table we'll convert into a DataTable
	var table = $('<table  class="display" width="100%"/>');

	// Display it the child row
	row.child(table).show();

	console.log(level);
	if (level == 1) {
		$.ajax({
			type: "POST",
			async: false,
			url: "/demofetch2/",
			headers: {
				"X-CSRFToken": csrftoken,
			},
			success: function (data) {
				getResponse(data); // pass parameters
				//tempData = data;
			},
		});
	}

	function getResponse(response) {
		tempData = response;
	}
	console.log(keyName);
	if (keyName == "areaId") {
		rawParams = findNestedObj(tempData, keyName, rowId);
		trData = rawParams.objects.map((doc) => Object(doc));
		lvl2Data = trData;

		var usersTable = table.DataTable({
			dom: "rt",
			data: trData,
			columns: [
				{
					className: "dt-control",
					orderable: false,
					data: null,
					defaultContent: "",
					width: "1%",
				},
				// { data: 'sAreaId', width:"5%" },
				{ title: "CODE", data: "objCode" },
				{ title: "OBJECTS", data: "ObjName" },
				{
					data: null,
					defaultContent:
						'<button class="btn btn-default  btn-obj-edit"><i class="fas fa-edit"></i></button> ' +
						'<button class="btn  btn-default btn-obj-del"> <i class="fa fa-trash" aria-hidden="true"></i></button> ',
					targets: -1,
					width: "15%",
				},
			],
		});
	} else {
		rawParams = findNestedObj(lvl2Data, keyName, rowId);
		console.log(rawParams);
		trData = rawParams.indicator.map((doc) => Object(doc));

		var usersTable = table.DataTable({
			dom: "rt",
			data: trData,
			columns: [
				{ title: "CODE", data: "manCode" },
				{ title: "INDICATORS", data: "manDef" },

				{
					data: null,
					defaultContent:
						'<button class="btn btn-default btn-ind-edit "> <i class="fas fa-edit"></i></button> ' +
						'<button class="btn  btn-default btn-ind-del"> <i class="fa fa-trash" aria-hidden="true"></i></button> ',
					targets: -1,
					width: "15%",
				},
			],
		});
	}
	// Add event listener for opening and closing details
	table.on("click", "td.dt-control", function (e) {
		e.stopPropagation(); // Don't bubble up to parent event

		var tr = $(this).closest("tr");
		var row = usersTable.row(tr);

		if (row.child.isShown()) {
			// This row is already open - close it
			destroyChild(row);
			tr.removeClass("shown");
		} else {
			// Open this row

			// Simulate fetching data for child table
			var data = row.data();
			var rowData = {
				code: data.code,
			};

			console.log(data);
			if (level === 1) {
				rowData.level2 = "Level 2";
			} else if (level === 2) {
				rowData.level3 = "Level3";
			} else {
				rowData.other = "Other stuff";
			}

			keyName = Object.keys(data)[1]; // objId

			createChild(row, rowData, keyName, data.objId, level + 1);
			tr.addClass("shown");
		}
	});
}

function destroyChild(row) {
	// Remove and destroy the DataTable in the child row
	var table = $("table", row.child());
	table.detach();
	table.DataTable().destroy();

	// And then hide the row
	row.child.hide();
}

$(document).ready(function () {
	var areaId = "";
	var objId = "";
	var indId = "";

	var siteTable = $("#example").DataTable({
		ajax: "/demofetch2/",
		rowId: "areaId",
		order: [1, "asc"],
		columns: [
			{
				className: "dt-control",
				orderable: false,
				data: null,
				defaultContent: "",
				width: "1px",
			},
			{ data: "areaId", width: "5%" },
			{ title: "CODE", data: "code" },
			{ title: "AREA", data: "area" },
			{
				data: null,
				defaultContent:
					'<button class="btn edit-area btn-default" > <i class="fas fa-edit"></i></button> ' +
					'<button class="btn delete-area btn-default "> <i class="fa fa-trash" aria-hidden="true"></i></button> ',
				targets: -1,
				width: "15%",
			},
		],
		select: {
			style: "os",
			selector: "td:not(:first-child)",
		},
	});

	// Add event listener for opening and closing details
	$("#example tbody").on("click", "td.dt-control", function () {
		var tr = $(this).closest("tr");
		var row = siteTable.row(tr);
		var ctr = 1;
		if (row.child.isShown()) {
			// This row is already open - close it
			destroyChild(row);
			tr.removeClass("shown");
		} else {
			// Open this row

			var data = row.data();

			// Simulate fetching data for child table
			var rowData = {
				code: data.code,
				area: data.area,
			};

			keyName = Object.keys(data)[0]; //areaId

			createChild(row, rowData, keyName, data.areaId, ctr);
			tr.addClass("shown");
			ctr++;
		}
	});

	//------------------------------ AREA ------------------------------
	// add
	$("#area-add-form").on("submit", function (e) {
		e.preventDefault();
		e.stopPropagation();
		var $this = $(this);
		var valid = true;

		$("#area-add-form input").each(function () {
			let $this = $(this);
			var currentInputVal = $this.val();
			if (currentInputVal == null || currentInputVal == "") {
				valid = false;
				$this
					.parent(".validate")
					.find(".mySpan")
					.text(
						"The " +
							$this.attr("name").replace(/[\_]+/g, " ") +
							"field is required"
					);
			} else {
				$this.parent(".validate").find(".mySpan").text("");
			}
		});
		console.log(valid);
		if (valid) {
			$(".btn-save").text("Saving...").attr("disabled", true);
			let data = $this.serialize();

			console.log(data);
			$.ajax({
				url: $(".btn-save").data("url"),
				type: "POST",
				data: data,
				dataType: "json",
				success: function (data) {
					if (data.Status == "Saved") {
						Swal.fire({
							position: "center",
							icon: "success",
							title: "Record Successfully Saved!",
							showConfirmButton: false,
							timer: 1500,
						});

						$(".btn-save").text("Save").attr("disabled", false);

						$this[0].reset();

						$("#example").DataTable().ajax.reload();
					} else {
						Swal.fire({
							position: "center",
							icon: "error",
							title: "Failed to Save Record!",
							showConfirmButton: false,
							timer: 1500,
						});
					}
				},
				error: function (data) {
					Swal.fire({
						position: "center",
						icon: "error",
						title: "Error Occured!",
						showConfirmButton: false,
						timer: 1500,
					});
				},
			});
		}
		return false;
	});
	//edit
	siteTable.on("click", ".edit-area", function (e) {
		e.preventDefault();
		e.stopPropagation();
		let data = siteTable.row(e.target.closest("tr")).data();

		areaId = data.areaId;
		$("#area-edit-form input[name='code']").val(data.code);
		$("#area-edit-form input[name='name']").val(data.area);
		$("#modal-area-edit-lg").modal("show");
	});
	$("#area-edit-form").on("submit", function (e) {
		e.preventDefault();
		e.stopPropagation();

		var $this = $(this);
		var valid = true;

		$("#area-edit-form input").each(function () {
			let $this = $(this);
			var currentInputVal = $this.val();

			if (currentInputVal == null || currentInputVal == "") {
				valid = false;
				$this
					.parent(".validate")
					.find(".mySpan")
					.text(
						"The " +
							$this.attr("name").replace(/[\_]+/g, " ") +
							"field is required"
					);
			} else {
				$this.parent(".validate").find(".mySpan").text("");
			}
		});

		if (valid) {
			$(".btn-save").text("Saving...").attr("disabled", true);
			let data = $this.serialize();
			// var editUrl = '{% url "keyResultAreaUpdate" id=0 %}'.replace("0", areaId);
			var editUrl = $(".btn-update").data("url");

			$.ajax({
				url: editUrl.replace("0", areaId),
				type: "POST",
				data: data,
				dataType: "json",
				success: function (data) {
					console.log(data.Status);
					if (data.Status == "Updated") {
						Swal.fire({
							position: "center",
							icon: "success",
							title: "Record Successfully Updated!",
							showConfirmButton: false,
							timer: 1500,
						});

						$(".btn-save").text("Save").attr("disabled", false);
						$("#example").DataTable().ajax.reload();
						$("#modal-area-edit-lg").modal("hide");
					} else {
						Swal.fire({
							position: "center",
							icon: "error",
							title: "Failed to Update Record!",
							showConfirmButton: false,
							timer: 1500,
						});
					}
				},
				error: function (data) {
					Swal.fire({
						position: "center",
						icon: "error",
						title: "Error Occured!",
						showConfirmButton: false,
						timer: 1500,
					});
				},
			});
		}
	});
	//Delete
	siteTable.on("click", ".delete-area", function (e) {
		let data = siteTable.row(e.target.closest("tr")).data();
		areaId = data.areaId;
		const element = document.getElementById("area-name");
		element.innerHTML =
			"<h5>Code: " + data.code + "</h5>" + "  Area: " + data.area;

		$("#modal-area-del-lg").modal("show");
	});
	$("#area-del-form").on("submit", function (e) {
		e.preventDefault();
		e.stopPropagation();
		siteTable.row($(this).parents("tr")).remove().draw();
		var delUrl = $(".btn-delete").data("url");

		$.ajax({
			url: delUrl.replace("0", areaId),
			method: "POST",
			success: function (data) {
				if (data.Status == "Deleted") {
					Swal.fire({
						position: "center",
						icon: "success",
						title: "Record Successfully Deleted!",
						showConfirmButton: false,
						timer: 1500,
					});
					$("#example").DataTable().ajax.reload();
					$("#modal-area-del-lg").modal("hide");
				} else {
					Swal.fire({
						position: "center",
						icon: "error",
						title: "Failed to Delete Record!",
						showConfirmButton: false,
						timer: 1500,
					});
				}
			},
			error: function (data) {
				Swal.fire({
					position: "center",
					icon: "error",
					title: "Error Occured!",
					showConfirmButton: false,
					timer: 1500,
				});
			},
		});
	});
	//-------------------------------------------------------------------

	//---------------------- Strategic Objective ------------------------
	//on click event
	$("#example").on("draw.dt", function (e, settings) {
		var subtable = $("#" + settings.nTable.id + "").DataTable();
		var nTable = "#" + settings.nTable.id + "";
		// Objective click event
		$("#" + settings.nTable.id + "").on("click", ".btn-obj-edit", function (e) {
			e.preventDefault();
			e.stopPropagation();

			let data = subtable.row(e.target.closest("tr")).data();
			console.log(data);
			objId = data.objId;
			$("#obj-edit-form input[name='code']").val(data.objCode);
			$("#obj-edit-form textarea[name='definition']").val(data.ObjName);
			$("#modal-obj-edit-lg").modal("show");
		});

		$("#" + settings.nTable.id + "").on("click", ".btn-obj-del", function (e) {
			e.preventDefault();
			e.stopPropagation();

			let data = subtable.row(e.target.closest("tr")).data();
			objId = data.objId;
			const element = document.getElementById("obj-name");
			element.innerHTML =
				"<h5>Code: " + data.objCode + "</h5>" + "  Objective: " + data.ObjName;
			$("#modal-obj-del-lg").modal("show");
		});

		// indicator click event
		$(nTable).on("click", ".btn-ind-edit", function (e) {
			e.preventDefault();
			e.stopPropagation();
			let data = subtable.row(e.target.closest("tr")).data();
			console.log(data);
			indId = data.manId;
			objId = data.objId;
			$("#ind-edit-form input[name='code']").val(data.manCode);
			$("#ind-edit-form textarea[name='description']").val(data.manDef);
			$("#modal-ind-edit-lg").modal("show");
			console.log(nTable);
		});

		$(nTable).on("click", ".btn-ind-del", function (e) {
			e.preventDefault();
			e.stopPropagation();

			let data = subtable.row(e.target.closest("tr")).data();
			indId = data.manId;
			const element = document.getElementById("ind-name");
			element.innerHTML =
				"<h5>Code: " + data.manCode + "</h5>" + "  Indicator: " + data.manDef;
			$("#modal-ind-del-lg").modal("show");
		});
	});

	//CRUD FUNCTIONS
	//add
	$("#obj-add-form").on("submit", function (e) {
		e.preventDefault();
		e.stopPropagation();
		var $this = $(this);
		var valid = true;

		console.log(valid);
		$("#obj-add-form input").each(function () {
			let $this = $(this);
			var currentInputVal = $this.val();
			if (currentInputVal == null || currentInputVal == "") {
				valid = false;
				$this
					.parent(".validate")
					.find(".mySpan")
					.text(
						"The " +
							$this.attr("name").replace(/[\_]+/g, " ") +
							"field is required"
					);
			} else {
				$this.parent(".validate").find(".mySpan").text("");
			}
		});

		if ($.trim($("#id_definition").val()).length < 1) {
			console.log("empty");
			valid = false;
			$("#obj-add-form textarea")
				.parent(".validate")
				.find(".mySpan")
				.text("This field is required");
		} else {
			console.log("des1");
			$("#obj-add-form textarea").parent(".validate").find(".mySpan").text("");
		}
		console.log(valid);
		if (valid) {
			$(".btn-obj-save").text("Saving...").attr("disabled", true);
			let data = $this.serialize();

			console.log(data);
			$.ajax({
				url: $(".btn-obj-save").data("url"),
				type: "POST",
				data: data,
				dataType: "json",
				success: function (data) {
					if (data.Status == "Saved") {
						Swal.fire({
							position: "center",
							icon: "success",
							title: "Record Successfully Saved!",
							showConfirmButton: false,
							timer: 1500,
						});

						$(".btn-obj-save").text("Save").attr("disabled", false);

						$this[0].reset();

						$("#example").DataTable().ajax.reload();
					} else {
						Swal.fire({
							position: "center",
							icon: "error",
							title: "Failed to Save Record!",
							showConfirmButton: false,
							timer: 1500,
						});
					}
				},
				error: function (data) {
					Swal.fire({
						position: "center",
						icon: "error",
						title: "Error Occured!",
						showConfirmButton: false,
						timer: 1500,
					});
				},
			});
		}
		return false;
	});

	//edit
	$("#obj-edit-form").on("submit", function (e) {
		e.preventDefault();
		e.stopPropagation();

		var $this = $(this);
		var valid = true;

		$("#obj-edit-form input").each(function () {
			let $this = $(this);
			var currentInputVal = $this.val();

			if (currentInputVal == null || currentInputVal == "") {
				valid = false;
				$this
					.parent(".validate")
					.find(".mySpan")
					.text(
						"The " +
							$this.attr("name").replace(/[\_]+/g, " ") +
							"field is required"
					);
			} else {
				valid = true;
				$this.parent(".validate").find(".mySpan").text("");
			}
		});

		// if ($.trim($("#id_definition").val()).length < 1) {
		// 	valid = false;
		// 	$("#obj-edit-form textarea")
		// 		.parent(".validate")
		// 		.find(".mySpan")
		// 		.text("This field is required");
		// } else {
		// 	$("#obj-edit-form textarea").parent(".validate").find(".mySpan").text("");
		// }

		if (valid) {
			$(".btn-obj-update").text("Updating...").attr("disabled", true);
			let data = $this.serialize();
			var editUrl = $(".btn-obj-update").data("url");

			$.ajax({
				url: editUrl.replace("0", objId),
				type: "POST",
				data: data,
				dataType: "json",
				success: function (data) {
					console.log(data.Status);
					if (data.Status == "Updated") {
						Swal.fire({
							position: "center",
							icon: "success",
							title: "Record Successfully Updated!",
							showConfirmButton: false,
							timer: 1500,
						});

						$(".btn-obj-update").text("Update").attr("disabled", false);
						$("#example").DataTable().ajax.reload();
						$("#modal-obj-edit-lg").modal("hide");
					} else {
						Swal.fire({
							position: "center",
							icon: "error",
							title: "Failed to Update Record!",
							showConfirmButton: false,
							timer: 1500,
						});
					}
				},
				error: function (data) {
					Swal.fire({
						position: "center",
						icon: "error",
						title: "Error Occured!",
						showConfirmButton: false,
						timer: 1500,
					});
				},
			});
		}
	});

	//delete
	$("#obj-del-form").on("submit", function (e) {
		e.preventDefault();
		e.stopPropagation();
		siteTable.row($(this).parents("tr")).remove().draw();
		var delUrl = $("#obj-del-form .btn-delete").data("url");
		$.ajax({
			url: delUrl.replace("0", objId),
			method: "POST",
			success: function (data) {
				if (data.Status == "Deleted") {
					Swal.fire({
						position: "center",
						icon: "success",
						title: "Record Successfully Deleted!",
						showConfirmButton: false,
						timer: 1500,
					});

					$("#example").DataTable().ajax.reload();
					$("#modal-obj-del-lg").modal("hide");
				} else {
					Swal.fire({
						position: "center",
						icon: "error",
						title: "Failed to Delete Record!",
						showConfirmButton: false,
						timer: 1500,
					});
				}
			},
			error: function (data) {
				Swal.fire({
					position: "center",
					icon: "error",
					title: "Error Occured!",
					showConfirmButton: false,
					timer: 1500,
				});
			},
		});
	});
	//-------------------------------------------------------------------

	//-------------------------- Indicator ------------------------------

	//add
	$("#ind-add-form").on("submit", function (e) {
		e.preventDefault();
		e.stopPropagation();
		var $this = $(this);
		var valid = true;

		console.log(valid);
		$("#ind-add-form input").each(function () {
			let $this = $(this);
			var currentInputVal = $this.val();
			if (currentInputVal == null || currentInputVal == "") {
				valid = false;
				$this
					.parent(".validate")
					.find(".mySpan")
					.text(
						"The " +
							$this.attr("name").replace(/[\_]+/g, " ") +
							"field is required"
					);
			} else {
				$this.parent(".validate").find(".mySpan").text("");
			}
		});

		// if ($.trim($("#id_definition").val()).length < 1) {
		// 	console.log("empty");
		// 	valid = false;
		// 	$("#obj-add-form textarea")
		// 		.parent(".validate")
		// 		.find(".mySpan")
		// 		.text("This field is required");
		// } else {
		// 	console.log("des1");
		// 	$("#obj-add-form textarea").parent(".validate").find(".mySpan").text("");
		// }
		console.log(valid);
		if (valid) {
			$(".btn-ind-save").text("Saving...").attr("disabled", true);
			let data = $this.serialize();

			console.log(data);
			$.ajax({
				url: $(".btn-ind-save").data("url"),
				type: "POST",
				data: data,
				dataType: "json",
				success: function (data) {
					if (data.Status == "Saved") {
						Swal.fire({
							position: "center",
							icon: "success",
							title: "Record Successfully Saved!",
							showConfirmButton: false,
							timer: 1500,
						});

						$(".btn-obj-save").text("Save").attr("disabled", false);

						$this[0].reset();

						$("#example").DataTable().ajax.reload();
					} else {
						Swal.fire({
							position: "center",
							icon: "error",
							title: "Failed to Save Record!",
							showConfirmButton: false,
							timer: 1500,
						});
					}
				},
				error: function (data) {
					Swal.fire({
						position: "center",
						icon: "error",
						title: "Error Occured!",
						showConfirmButton: false,
						timer: 1500,
					});
				},
			});
		}
		return false;
	});

	//edit
	$("#ind-edit-form").on("submit", function (e) {
		e.preventDefault();
		e.stopPropagation();

		var $this = $(this);
		var valid = true;

		$("#ind-edit-form input").each(function () {
			let $this = $(this);
			var currentInputVal = $this.val();

			if (currentInputVal == null || currentInputVal == "") {
				valid = false;
				$this
					.parent(".validate")
					.find(".mySpan")
					.text(
						"The " +
							$this.attr("name").replace(/[\_]+/g, " ") +
							"field is required"
					);
			} else {
				valid = true;
				$this.parent(".validate").find(".mySpan").text("");
			}
		});

		$("#ind-edit-form input").each(function () {
			let $this = $(this);
			var currentInputVal = $this.val();
			if (currentInputVal == null || currentInputVal == "") {
				valid = false;
				$this
					.parent(".validate")
					.find(".mySpan")
					.text(
						"The " +
							$this.attr("name").replace(/[\_]+/g, " ") +
							"field is required"
					);
			} else {
				$this.parent(".validate").find(".mySpan").text("");
			}
		});

		if (valid) {
			$(".btn-ind-update").text("Updating...").attr("disabled", true);
			let data = $this.serialize() + "&" + $.param({ sObjId: objId });

			var editUrl = $(".btn-ind-update").data("url");

			console.log(data);
			$.ajax({
				url: editUrl.replace("0", indId),
				type: "POST",
				data: data,
				dataType: "json",
				success: function (data) {
					console.log(data.Status);
					if (data.Status == "Updated") {
						Swal.fire({
							position: "center",
							icon: "success",
							title: "Record Successfully Updated!",
							showConfirmButton: false,
							timer: 1500,
						});

						$(".btn-ind-update").text("Update").attr("disabled", false);
						$("#example").DataTable().ajax.reload();
						$("#modal-ind-edit-lg").modal("hide");
					} else {
						Swal.fire({
							position: "center",
							icon: "error",
							title: "Failed to Update Record!",
							showConfirmButton: false,
							timer: 1500,
						});
					}
				},
				error: function (data) {
					Swal.fire({
						position: "center",
						icon: "error",
						title: "Error Occured!",
						showConfirmButton: false,
						timer: 1500,
					});
				},
			});
		}
	});

	//delete
	$("#ind-del-form").on("submit", function (e) {
		e.preventDefault();
		e.stopPropagation();
		siteTable.row($(this).parents("tr")).remove().draw();
		var delUrl = $("#ind-del-form .btn-ind-delete").data("url");
		$.ajax({
			url: delUrl.replace("0", indId),
			method: "POST",
			success: function (data) {
				if (data.Status == "Deleted") {
					Swal.fire({
						position: "center",
						icon: "success",
						title: "Record Successfully Deleted!",
						showConfirmButton: false,
						timer: 1500,
					});

					$("#example").DataTable().ajax.reload();
					$("#modal-ind-del-lg").modal("hide");
				} else {
					Swal.fire({
						position: "center",
						icon: "error",
						title: "Failed to Delete Record!",
						showConfirmButton: false,
						timer: 1500,
					});
				}
			},
			error: function (data) {
				Swal.fire({
					position: "center",
					icon: "error",
					title: "Error Occured!",
					showConfirmButton: false,
					timer: 1500,
				});
			},
		});
	});

	//-------------------------------------------------------------------
	$("#example").on("draw.dt", function (e, settings) {
		console.log("sites > DataTable > draw.dt [" + new Date() + "]");
		console.log("Table ID: ", settings.nTable.id);
	});
});
