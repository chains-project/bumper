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
        ),
        new StringContains("Unexpected path")
    );
}
```

The only change I made is to remove the `false` argument from the `StringContains` constructor. This is because the `StringContains` constructor with two arguments was removed in the new library version. The `StringContains` constructor with one argument is still available, so I used that instead.