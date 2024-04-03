Here's the proposed patch to fix the error:

```java
@Test
void shouldThrowExceptionOnInvalidPath() {
    StringContains stringContains = new StringContains("Unexpected path");
    MatcherAssert.assertThat(
        Assertions.assertThrows(
            IllegalArgumentException.class,
            () -> new UploadEntity.Request(
                new RequestLine(RqMethod.PUT, "/one/two").toString()
            ).name()
        ).getMessage(),
        stringContains
    );
}
```

In this patch, I created a variable `stringContains` to store the `StringContains` matcher, and passed it directly as an argument to `MatcherAssert.assertThat()` instead of creating a new `StringContains` matcher directly in the argument list. This resolves the error caused by the updated library version, which now requires a single argument for the `StringContains` constructor.