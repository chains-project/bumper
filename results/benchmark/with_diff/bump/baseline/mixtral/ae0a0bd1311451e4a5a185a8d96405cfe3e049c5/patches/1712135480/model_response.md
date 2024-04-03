Here's the fixed version of the failing method, taking into account the changes in the new library version:

```java
@Test
void shouldThrowExceptionOnInvalidPath() {
    MatcherAssert.assertThat(
        Assertions.assertThrows(
            IllegalArgumentException.class,
            () -> new UploadEntity.Request(
                new RequestLine(RqMethod.PUT, "/one/two").toString()
            ).name()
        ),
        new StringContains("Unexpected path")
    );
}
```

The issue was caused by the incorrect usage of the `StringContains` constructor. The new library version requires only a single argument for the `StringContains` constructor. I have removed the `false` argument from the `StringContains` constructor, which fixes the error.