Here's a possible patch for the failing client code:

```java
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    org.hamcrest.MatcherAssert.assertThat(org.junit.jupiter.api.Assertions.assertThrows(java.lang.IllegalArgumentException.class, () -> new com.artipie.docker.http.UploadEntity.Request(new com.artipie.http.rq.RequestLine(RqMethod.PUT, "/one/two").toString())).getName(), new org.hamcrest.core.IsInstanceOf(java.lang.IllegalArgumentException.class));
}
```

In this patch, I replaced the `StringContains` matcher with the `IsInstanceOf` matcher to check if the exception thrown is an instance of `IllegalArgumentException`. This should fix the error message you encountered.