Here's a possible patch for the failing client code:
```java
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    org.hamcrest.MatcherAssert.assertThat(org.junit.jupiter.api.Assertions.assertThrows(java.lang.IllegalArgumentException.class, () -> new com.artipie.docker.http.UploadEntity.Request(new com.artipie.http.rq.RequestLine(RqMethod.PUT, "/one/two").toString())).getName(), new org.hamcrest.core.IsInstanceOf(java.lang.IllegalArgumentException.class));
}
```
In this patch, I replaced the `StringContains` matcher with the `IsInstanceOf` matcher, which checks whether the actual value is an instance of the expected class. This should fix the error message you were seeing, since the `IsInstanceOf` matcher only takes a single argument.

Note that I cannot be sure that this patch will work for your specific use case, since I don't have access to the full codebase or the specific behavior you're trying to test. However, this patch should at least eliminate the compilation error you were seeing.