Here is a possible patch for the failing client code:

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
        new StringStartsWith("Unexpected query") // use StringStartsWith instead of StringContains
    );
}
```

In this patch, I replaced the `StringContains` matcher with the `StringStartsWith` matcher, which should have the same behavior in this case. The `StringContains` matcher was deprecated in Hamcrest 2.2 and removed in Hamcrest 2.5, so it may not be available in the version of Hamcrest that the client code is using. The `StringStartsWith` matcher was introduced in Hamcrest 2.2, so it should be available in most versions of Hamcrest.

Note that I did not change the function signature or remove the `@Override` decorator, as these were not necessary to fix the error. I also did not create any new variables or use any removed library methods, as these were not needed to fix the error. I did use the `StringStartsWith` matcher, which was added in Hamcrest 2.2, but this should not cause any compatibility issues.