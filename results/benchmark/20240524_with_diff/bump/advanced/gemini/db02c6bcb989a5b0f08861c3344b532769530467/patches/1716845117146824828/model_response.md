```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    assertThrows(
        org.junit.jupiter.api.Assertions::assertThrows,
        org.apache.http.client.HttpResponseException.class,
        () -> {
            new com.artipie.docker.http.UploadEntityRequest(
                new org.apache.http.entity.ByteArrayEntity(
                    new byte[]{0, 1, 2, 3, 4, 5, 6, 7, 8, 9},
                    "application/octet-stream"
                ),
                "http://localhost:8080/v1/images/create?fromSrc=https://example.com/image.tar",
                "Authorization",
                "Basic dXNlcjpwYXNzd29yZA=="
            ).execute(new org.apache.http.impl.client.CloseableHttpClient());
        }
    );
}
```