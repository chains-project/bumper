Here's a possible patch for the failing client code:
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
            ).digest()
        ).getMessage(),
        new StringStartsWith("Unexpected query") // replace 'StringContains' with 'StringStartsWith'
    );
}
```
The failure is caused by a change in the `StringContains` matcher, which now requires a single string argument instead of a boolean and a string. To fix the failure, we can replace the `StringContains` matcher with a new matcher, `StringStartsWith`, which checks if a string starts with a given substring. This matcher is added in the new library version (indicated by `++`). Note that the `StringStartsWith` matcher is used here just as an example, and you may need to adjust the matcher based on the specific requirement of your test case.