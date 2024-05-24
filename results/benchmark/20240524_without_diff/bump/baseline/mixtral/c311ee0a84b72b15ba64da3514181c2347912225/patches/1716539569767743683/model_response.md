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

In the original code, the `StringContains` matcher is used with two arguments, which is not supported in the new library version. To fix the error, I replaced `StringContains` with `StringStartsWith`, which only takes one argument and checks if a string starts with a given substring. This should have the same effect as the original code, but it is compatible with the new library version.