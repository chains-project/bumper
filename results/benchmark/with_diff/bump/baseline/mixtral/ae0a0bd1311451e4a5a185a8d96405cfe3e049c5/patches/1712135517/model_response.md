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

The `StringContains` constructor now requires a single string argument, so I removed the `false` argument.