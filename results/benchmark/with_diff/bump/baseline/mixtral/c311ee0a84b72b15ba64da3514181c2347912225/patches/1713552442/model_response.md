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

In this patch, I replaced the `StringContains` matcher with the `StringStartsWith` matcher, which has the same semantics but a different constructor signature. This should fix the error message you were seeing.

Note that this patch assumes that the behavior of the `name()` method has not changed in the new library version, and that it still returns a string that starts with the text "Unexpected path" when the path is invalid. If this assumption is incorrect, you may need to adjust the patch accordingly.