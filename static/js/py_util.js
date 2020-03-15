function isEmpty(obj) {
  return Object.keys(obj).length === 0;
}

var serializeArray = function (form) {

	// Setup our serialized data
	var serialized = [];
    //console.log(form);
    descendents = form.getElementsByTagName('*');
	// Loop through each field in the form
	for (var i = 0; i < descendents.length; i++) {

		var field = descendents[i];

		// Don't serialize fields without a name, submits, buttons, file and reset inputs, and disabled fields
		if (!field.name || field.disabled || field.type === 'file' || field.type === 'reset' || field.type === 'submit' || field.type === 'button') continue;

		// If a multi-select, get all selections
		if (field.type === 'select-multiple') {
			for (var n = 0; n < field.options.length; n++) {
				if (!field.options[n].selected) continue;
				serialized.push({
					name: field.name,
					value: field.options[n].value
				});
			}
		}

		// Convert field data to a query string
		else if ((field.type !== 'checkbox' && field.type !== 'radio') || field.checked) {
			serialized.push({
				name: field.name,
				value: field.value
			});
		}
	}

	return serialized;

};