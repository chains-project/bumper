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
        new StringContains("Unexpected path")
    );
}
```

The issue was caused by the incorrect usage of the `StringContains` matcher. In the new library version, the constructor for `StringContains` no longer accepts a `boolean` parameter. So, I've removed the `false` parameter from the `StringContains` constructor.