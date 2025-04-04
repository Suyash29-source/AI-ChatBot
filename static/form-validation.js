function validateForm() {
    const parentName = document.getElementById('parent_name').value.trim();
    const relation = document.getElementById('relation').value.trim();
    const fullName = document.getElementById('full_name').value.trim();
    const standard = document.getElementById('standard').value;
    const email = document.getElementById('email').value.trim();
    const phone = document.getElementById('phone').value.trim();

    let isValid = true;

    // Clear previous error messages
    clearErrors();

    // Check if required fields are filled
    if (!parentName) {
        showError('parent_name', 'Parent\'s name is required.');
        isValid = false;
    }
    if (!relation) {
        showError('relation', 'Relation is required.');
        isValid = false;
    }
    if (!fullName) {
        showError('full_name', 'Student\'s full name is required.');
        isValid = false;
    }
    if (standard === '') {
        showError('standard', 'Standard (Class) is required.');
        isValid = false;
    }
    if (!email) {
        showError('email', 'Email is required.');
        isValid = false;
    } else if (!validateEmail(email)) {
        showError('email', 'Please enter a valid email address.');
        isValid = false;
    }
    if (!phone) {
        showError('phone', 'Phone number is required.');
        isValid = false;
    } else if (!validatePhone(phone)) {
        showError('phone', 'Please enter a valid phone number.');
        isValid = false;
    }

    return isValid;
}

function showError(fieldId, message) {
    const field = document.getElementById(fieldId);
    const error = document.createElement('div');
    error.className = 'error-message';
    error.innerText = message;
    field.parentNode.insertBefore(error, field.nextSibling);
}

function clearErrors() {
    const errorMessages = document.querySelectorAll('.error-message');
    errorMessages.forEach(error => error.remove());
}

function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(String(email).toLowerCase());
}

function validatePhone(phone) {
    const re = /^[0-9]{10}$/; // Assuming a 10-digit phone number
    return re.test(String(phone));
}