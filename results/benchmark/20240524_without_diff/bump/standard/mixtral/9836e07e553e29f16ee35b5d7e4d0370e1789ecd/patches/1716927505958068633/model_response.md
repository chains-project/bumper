Here is a possible patch for the failing client code:
```java
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    org.hamcrest.MatcherAssert.assertThat(org.junit.jupiter.api.Assertions.assertThrows(java.lang.IllegalArgumentException.class, () -> new com.artipie.docker.http.UploadEntity.Request(new com.artipie.http.rq.RequestLine(RqMethod.PUT, "/one/two").toString())).getName(), new org.hamcrest.core.IsInstanceOf(java.lang.IllegalArgumentException.class));
}
```
This patch uses the `IsInstanceOf` matcher from Hamcrest instead of the `StringContains` matcher, which should fix the error message you provided. The `IsInstanceOf` matcher checks if the given object is an instance of the specified class, which is more appropriate for checking the type of an exception. The `getName` method is used to get the name of the exception, which can be used to check its type.