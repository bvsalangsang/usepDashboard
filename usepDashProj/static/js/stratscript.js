const csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;
var areaId;
var areaName;

function loadStrat(stratId) {
	$.ajax({
		async: false,
		url: "/strat-get/" + stratId,
		dataType: "json",
		success: function (data) {
			year = data.data[0].targetyr;
			createdBy = data.data[0].createdBy;
			description = data.data[0].description;
			$(".year-created").html(year);
			$(".created-by").html(createdBy);
			$(".description").html(description);
		},
	});
}

function createChild(row, rowData, keyName, rowId, level, tempstratId) {
	var numLevels = 2; // Number of child levels with .details-control
	var trData;

	// This is the table we'll convert into a DataTable
	var table = $('<table  class="display" width="100%"/>');

	// Display it the child row
	row.child(table).show();

	console.log(level);
	fetchUrl = "/stratFetch/" + tempstratId;

	if (level == 1) {
		$.ajax({
			type: "POST",
			async: false,
			url: fetchUrl,
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

	console.log(tempData);
	if (keyName == "areaId") {
		console.log("rowId: " + rowId);
		var targetAreaId = rowId;
		// rawParams = findNestedObj(tempData, keyName, rowId);
		// trData = rawParams.objects.map((doc) => Object(doc));
		indexId = rowId - 1;
		var trData = [];
		$.each(tempData.data[indexId].objects, function (index, value) {
			if (value.sAreaId === targetAreaId) {
				trData.push(value);
			}
		});

		areaId = rowData.areaId;
		areaName = rowData.area;
		lvl2Data = trData;
		// console.log(trData);

		var usersTable = table.DataTable({
			bFilter: false,
			bPaginate: false,
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
			layout: {
				topStart: {
					buttons: [
						{
							text: "+ SO",
							action: function (e, dt, node, config) {
								console.log(areaName);
								$(".area-name").html(areaName);
								$.ajax({
									url: "/ObjPerAreaJsonList/" + areaId,
									dataType: "json",
									success: function (response) {
										// Assuming response is an object
										console.log(response);
										var select = $("#test-obj");

										// Add clear option
										select.append(
											$("<option>", {
												value: "",
												text: "",
											})
										);

										response.data.forEach(function (item) {
											select.append(
												$("<option>", {
													value: item.sObjId,
													text: item.definition,
												})
											);
										});
									},
									error: function (xhr, status, error) {
										console.error(xhr.responseText);
									},
								});

								$("#modal-strat-obj-lg").modal("show");
							},
						},
					],
				},
			},
		});
	} else {
		var indicators = [];
		var targetObjId = rowData.objId;
		$.each(tempData.data[0].objects, function (index, value) {
			if (value.objId === targetObjId) {
				$.each(value.indicator, function (index, indicator) {
					indicators.push(indicator);
				});
			}
		});
		console.log(indicators);
		var groupColumn = 0;
		var usersTable = table.DataTable({
			bFilter: false,
			bPaginate: false,
			data: indicators,
			columns: [
				{ title: "TYPE", data: "type" },
				{ title: "CODE", data: "manCode" },
				{ title: "INDICATOR", data: "manDef" },
				{ title: "REFERENCE", data: "manRef" },
				{ title: "TARGET", data: "manTarget" },
				{ title: "ACTUAL", data: "manActual" },
				{ title: "VARIANCE", data: "manVar" },
				{ title: "PERCENT", data: "manPercent" },
				{
					title: "ACTION",
					data: null,
					defaultContent:
						'<button class="btn btn-default btn-ind-edit "> <i class="fas fa-edit"></i></button> ' +
						'<button class="btn  btn-default btn-ind-del"> <i class="fa fa-trash" aria-hidden="true"></i></button> ',
					targets: -1,
					width: "15%",
				},
			],
			columnDefs: [{ visible: false, targets: groupColumn }],
			order: [[groupColumn, "asc"]],
			displayLength: 25,
			drawCallback: function (settings) {
				var api = this.api();
				var rows = api.rows({ page: "current" }).nodes();
				var last = null;

				api
					.column(groupColumn, { page: "current" })
					.data()
					.each(function (group, i) {
						if (last !== group) {
							$(rows)
								.eq(i)
								.before(
									'<tr class="group"><td colspan="8"><h5>' +
										group +
										"</h5></td></tr>"
								);

							last = group;
						}
					});
			},
			layout: {
				topStart: {
					buttons: [
						{
							text: "+ KPI",
							action: function (e, dt, node, config) {
								$("#modal-strat-ind-lg").modal("show");
							},
						},
					],
				},
			},
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
			var data = row.data();
			var rowData = {
				objId: data.objId,
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

			console.log(rowData);
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

$(document).ready(function () {
	var onChangeValDetArea;
	var onChangeValDetObj;
	var tempstratId = sessionStorage.getItem("stratId");
	loadStrat(tempstratId);

	$(".select2bs4").select2({
		theme: "bootstrap4",
	});

	$("#det-area").on("change", function (e) {
		$.ajax({
			url: "/strat-get-area/" + $("#det-area").val(),
			dataType: "json",
			success: function (data) {
				onChangeValDetArea = data;
			},
		});
	});

	$("#test-obj").on("change", function (e) {
		console.log("/strat-get-obj/" + $("#det-obj").val());
		$.ajax({
			//replace to get
			url: "/strat-get-obj/" + $("#det-obj").val(),
			dataType: "json",
			success: function (data) {
				onChangeValDetObj = data;
				console.log(onChangeValDetObj);
			},
		});
	});

	fetchUrl = "/stratFetch/" + tempstratId;

	console.log(fetchUrl);

	var siteTable = $("#example").DataTable({
		ajax: fetchUrl,
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
		layout: {
			topStart: {
				buttons: [
					{
						text: "+ KRA",
						action: function (e, dt, node, config) {
							$("#modal-strat-area-lg").modal("show");
						},
					},
				],
			},
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
				areaId: data.areaId,
				code: data.code,
				area: data.area,
			};

			keyName = Object.keys(data)[0]; //areaId

			createChild(row, rowData, keyName, data.areaId, ctr, tempstratId);
			tr.addClass("shown");
			ctr++;
		}
	});

	//------------------------------ AREA ------------------------------
	// add
	$("#strat-area-form").on("submit", function (e) {
		e.preventDefault();
		e.stopPropagation();
		var $this = $(this);

		// tempStratId = stratId;
		// tempAreaId = onChangeVal.data[0].sAreaId;
		// tempDes = onChangeVal.data[0].name;

		$(".btn-save").text("Saving...").attr("disabled", true);

		data =
			$this.serialize() +
			"&" +
			$.param({
				stratId: tempstratId,
				description: onChangeValDetArea.data[0].name,
			});
		console.log(data);
		$.ajax({
			url: $(".btn-save").data("url"),
			type: "POST",
			data: data,
			dataType: "json",
			headers: {
				"X-CSRFToken": csrftoken,
			},
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
					$("#modal-strat-area-lg").show("hide");
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
			error: function (xhr) {
				console.log(xhr);
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

	//------------------------------ Objects ------------------------------
	// add
	$("#strat-obj-form").on("submit", function (e) {
		e.preventDefault();
		e.stopPropagation();
		var $this = $(this);

		$(".btn-obj-save").text("Saving...").attr("disabled", true);

		data =
			$this.serialize() +
			"&" +
			$.param({
				description: onChangeValDetObj.data[0].definition,
				sAreaId: areaId,
			});

		console.log(data);
		$.ajax({
			url: $(".btn-obj-save").data("url"),
			type: "POST",
			data: data,
			dataType: "json",
			headers: {
				"X-CSRFToken": csrftoken,
			},
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
					$("#modal-strat-obj-lg").modal("hide");
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
			error: function (xhr) {
				console.log(xhr);
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

	//------------------------------ Indicator ------------------------------
	// add
	$("#strat-ind-form").on("submit", function (e) {
		e.preventDefault();
		e.stopPropagation();
		var $this = $(this);
		data =
			$this.serialize() +
			"&" +
			$.param({
				description: "sample",
			});

		console.log(data);

		data;
		$.ajax({
			url: $(".btn-ind-save").data("url"),
			type: "POST",
			data: data,
			dataType: "json",
			headers: {
				"X-CSRFToken": csrftoken,
			},
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
					$("#modal-strat-ind-lg").modal("hide");
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
			error: function (xhr) {
				console.log(xhr);
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
});
