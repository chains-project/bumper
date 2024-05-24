Here's a proposed patch for the failing client code:

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

The failure is caused by the incorrect use of the `StringContains` matcher. The `StringContains` constructor requires a single argument (a `String`), but it is being called with two arguments (a `boolean` and a `String`).

In this case, it seems like the intent is to check if the message starts with the string "Unexpected query". To achieve this, you can replace `StringContains` with `StringStartsWith`, which checks if a string starts with a specific substring.