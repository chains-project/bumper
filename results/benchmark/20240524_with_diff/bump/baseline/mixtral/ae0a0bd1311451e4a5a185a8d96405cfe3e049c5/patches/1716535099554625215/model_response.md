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
                )
            ).getMessage(),
            new StringStartsWith("Unexpected query") // replace 'StringContains' with 'StringStartsWith'
        );
    }
```
The failure is caused by the incorrect usage of the `StringContains` matcher, which expects only one argument. In the new library version, a new `StringStartsWith` matcher has been added, which can be used to check if a string starts with a given substring.