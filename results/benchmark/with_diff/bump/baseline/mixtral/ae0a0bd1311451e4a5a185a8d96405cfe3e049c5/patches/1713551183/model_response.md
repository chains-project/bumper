Here's the proposed patch for the failing method:

```java
@Test
void shouldThrowExceptionOnInvalidPath() {
    MatcherAssert.assertThat(
        Assertions.assertThrows(
            IllegalArgumentException.class,
            () -> new UploadEntity.Request(
                new RequestLine(RqMethod.PUT, "/one/two")
            ).name()
        ).getMessage(),
        new StringContains("Unexpected path")
    );
}
```

The change made is in the `new StringContains` constructor. The `false` argument has been removed, as it is not needed and is causing a compilation error with the new library version.