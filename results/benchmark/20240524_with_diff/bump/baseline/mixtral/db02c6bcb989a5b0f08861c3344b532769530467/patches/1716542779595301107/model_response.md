Here's the fixed version of the failing method:

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

In the new library version, the constructor of `StringContains` has been changed to only accept a single argument, a `String`. Therefore, I replaced `new StringContains(false, "Unexpected path")` with `new StringStartsWith("Unexpected path")`, which checks if the given string starts with the specified substring.