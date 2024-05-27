```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    // Create a new instance of the UploadEntityRequest class.
    UploadEntityRequest uploadEntityRequest = new UploadEntityRequest(
            new java.net.URI("http://localhost:8080/v2/"),
            new java.io.File("/tmp/test.tar"),
            1024 * 1024
    );

    // Create a new instance of the HttpURLConnection class.
    HttpURLConnection connection = (HttpURLConnection) new java.net.URL("http://localhost:8080/v2/").openConnection();

    // Set the request method to POST.
    connection.setRequestMethod("POST");

    // Set the request headers.
    connection.setRequestProperty("Content-Type", "application/x-tar");

    // Create a new instance of the OutputStream class.
    OutputStream outputStream = connection.getOutputStream();

    // Write the contents of the file to the OutputStream.
    try (InputStream inputStream = new FileInputStream(uploadEntityRequest.getFile())) {
        byte[] buffer = new byte[1024];
        int bytesRead;
        while ((bytesRead = inputStream.read(buffer)) != -1) {
            outputStream.write(buffer, 0, bytesRead);
        }
    }

    // Close the OutputStream.
    outputStream.close();

    // Get the response code.
    int responseCode = connection.getResponseCode();

    // Assert that the response code is 400.
    assertThat(responseCode).isEqualTo(400);

    // Get the response message.
    String responseMessage = connection.getResponseMessage();

    // Assert that the response message is "Bad Request".
    assertThat(responseMessage).isEqualTo("Bad Request");

    // Close the connection.
    connection.disconnect();
}
```