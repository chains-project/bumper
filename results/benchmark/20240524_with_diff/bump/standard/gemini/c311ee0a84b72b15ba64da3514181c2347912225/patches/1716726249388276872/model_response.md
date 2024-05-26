```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    // TODO: review this AI generated patch!
    String path = "invalid-path";
    try {
        new org.apache.http.client.methods.HttpGet(path);
        org.junit.jupiter.api.Assertions.fail("Expected exception not thrown");
    } catch (org.apache.http.client.utils.URIBuilderException e) {
        // TODO: review this AI generated patch!
        org.junit.jupiter.api.Assertions.assertEquals("Invalid path: " + path, e.getMessage());
    }
}
```