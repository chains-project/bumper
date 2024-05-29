Here is a possible patch for the failing client code:
```java
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    StringContains matcher = new StringContains("Unexpected path");
    org.hamcrest.MatcherAssert.assertThat(org.junit.jupiter.api.Assertions.assertThrows(java.lang.IllegalArgumentException.class, () -> new com.artipie.docker.http.UploadEntity.Request(new com.artipie.http.rq.RequestLine(RqMethod.PUT, "/one/two").toString()).name()).getMessage(), matcher);
}
```
The patch creates a `StringContains` matcher object before the `assertThat` call, and passes it as an argument to the method. This way, the `StringContains` constructor is called with the correct number of arguments.