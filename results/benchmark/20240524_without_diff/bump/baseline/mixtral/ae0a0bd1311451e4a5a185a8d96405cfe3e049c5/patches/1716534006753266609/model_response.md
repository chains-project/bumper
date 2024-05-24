Here is a possible patch for the failing client code:

```java
@Test
void shouldThrowExceptionOnInvalidPath() {
    MatcherAssert.assertThat(
        Assertions.assertThrows(
            IllegalArgumentException.class,
            () -> new UploadEntity.Request(
                new RequestLine(RqMethod.PUT, "/one/two").toString()
            ).name()
        ).getMessage(),
        new StringStartsWith("Unexpected path")
    );
}
```

In this patch, I replaced the `StringContains` matcher with the `StringStartsWith` matcher, which only takes a single argument (the expected prefix of the actual string). This should fix the error message you were seeing.

Note that this patch assumes that the error message you want to check for starts with the string "Unexpected path". If this is not the case, you will need to adjust the argument to `StringStartsWith` accordingly.