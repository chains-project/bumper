Here is the fixed version of the failing method:

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
        new StringContains("Unexpected path")
    );
}
```

The only change made is in the `new StringContains` constructor call, where the second argument is now just a string literal instead of a `StringContains` object with a `false` argument. This is because the constructor signature for `StringContains` has changed in the new library version, and now only takes a single string argument instead of a boolean and a string.