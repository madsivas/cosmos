_i18n = function(textKey) {

    if (textKey instanceof Array) {
        var n = arguments[2];
        if (textKey.length === 2) {
            textKey = textKey[n === 1 ? 0 : 1];
        } else {
            textKey = textKey[n === 0 ? 0 : n === 1 ? 1 : 2];
        }
    }
    if (textKey === "") {
        return "";
    }

    var text;
    if (_i18n_catalog[textKey]) {
        text = _i18n_catalog[textKey];
    } else {
        logging.debug('i18n', 'textelement "'+textKey+'" not found in catalog, please run textupdate.');
        text = textKey;
    }

    for (var i = 1; i < arguments.length; i++) {
        var parts = text.split("%" + (i - 1));
        text = parts.join(arguments[i]);
    }

    return text;
}
