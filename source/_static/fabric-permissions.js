const NAMESPACE_CHARACTERS = 'abcdefghijklmnopqrstuvwxyz0123456789.-';
const PATH_CHARACTERS = NAMESPACE_CHARACTERS + '/';

function encodePermissionPart(value, allowSlash) {
    const allowed = allowSlash ? PATH_CHARACTERS : NAMESPACE_CHARACTERS;
    const bytes = new TextEncoder().encode(value.toLowerCase());
    let encoded = '';
    for (const byte of bytes) {
        const character = String.fromCharCode(byte);
        encoded += allowed.includes(character)
            ? character
            : '_' + byte.toString(16).padStart(2, '0');
    }
    return encoded;
}

function convertPermission(permission) {
    const separator = permission.indexOf('.');
    if (separator < 1 || separator === permission.length - 1) {
        return null;
    }
    const namespace = encodePermissionPart(permission.slice(0, separator), false);
    const path = encodePermissionPart(permission.slice(separator + 1), true);
    return {
        identifier: namespace + ':' + path,
        traditional: namespace + '.' + path,
    };
}

function showPermissionConversion(inputId, identifierId, traditionalId) {
    const identifier = document.getElementById(identifierId);
    const traditional = document.getElementById(traditionalId);
    const result = convertPermission(document.getElementById(inputId).value.trim());

    identifier.value = result === null ? '' : result.identifier;
    traditional.value = result === null ? '' : result.traditional;
}
