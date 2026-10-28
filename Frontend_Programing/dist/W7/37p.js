function getStatus(code) {
    switch (code) {
        case 200:
            return "Success";
        case 404:
            return "Not Found";
        case 500:
            return "Server Error";
        default:
            return "Unknown Status";
    }
}
console.log(getStatus(200)); // Success
console.log(getStatus(404)); // Not Found
console.log(getStatus(500)); // Server Error
export {};
