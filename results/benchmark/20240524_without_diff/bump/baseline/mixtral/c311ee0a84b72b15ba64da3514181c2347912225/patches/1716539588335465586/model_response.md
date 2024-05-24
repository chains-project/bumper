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

The only change I made is to remove the `false` argument from the `StringContains` constructor. It seems that the `StringContains` constructor no longer accepts a `boolean` argument in the new library version.