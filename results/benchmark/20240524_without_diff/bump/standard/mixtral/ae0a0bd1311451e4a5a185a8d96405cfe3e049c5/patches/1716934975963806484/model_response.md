Here's a possible patch for the failing client code:
```java
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    org.hamcrest.MatcherAssert.assertThat(org.junit.jupiter.api.Assertions.assertThrows(java.lang.IllegalArgumentException.class, () -> new com.artipie.docker.http.UploadEntity.Request(new com.artipie.http.rq.RequestLine(RqMethod.PUT, "/one/two").toString())).name(), new org.hamcrest.core.StringContains("Unexpected path"));
}
```
The change I made is to remove the `false` argument from the `StringContains` constructor. Based on the error message, it looks like this argument was added in a recent version of Hamcrest, but the code you provided was written for an older version that didn't have this argument. By removing it, the code should now be compatible with both old and new versions of Hamcrest.