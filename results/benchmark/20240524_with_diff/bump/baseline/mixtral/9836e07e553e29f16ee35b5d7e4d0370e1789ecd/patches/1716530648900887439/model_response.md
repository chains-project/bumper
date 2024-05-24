Here is a possible patch for the failing code:
```java
@Test
void shouldThrowExceptionWhenDigestIsAbsent() {
    MatcherAssert.assertThat(
        Assertions.assertThrows(
            IllegalStateException.class,
            () -> new UploadEntity.Request(
                new RequestLine(
                    RqMethod.PUT,
                    "/v2/my-repo/blobs/uploads/123-abc?what=nothing"
                ).toString()
            )
        ).getMessage(),
        new StringContains("Unexpected query") // removed 'false' argument
    );
}
```
Explanation:
The error message indicates that the `StringContains` constructor is expecting a single string argument, but it is receiving two arguments (a boolean and a string). The boolean argument was added in a newer version of the library, but the code is still using the old constructor. To fix the error, we can simply remove the boolean argument and keep only the string argument.