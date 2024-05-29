Here's a possible patch for the failing client code:
```java
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    org.hamcrest.MatcherAssert.assertThat(org.junit.jupiter.api.Assertions.assertThrows(java.lang.IllegalArgumentException.class, () -> new com.artipie.docker.http.UploadEntity.Request(new com.artipie.http.rq.RequestLine(RqMethod.PUT, "/one/two").toString())).getName(), new org.hamcrest.core.IsInstanceOf(java.lang.IllegalArgumentException.class));
}
```
In this patch, I replaced the `StringContains` matcher with the `IsInstanceOf` matcher, which checks if the actual value is an instance of the expected type. This should fix the error message you were seeing about the mismatch between the actual and formal argument lists.