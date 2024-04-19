Here's the updated method with the fix:

```java
@Test
void shouldThrowExceptionOnInvalidPath() {
    boolean contains = Assertions.assertThrows(
            IllegalArgumentException.class,
            () -> new UploadEntity.Request(
                    new RequestLine(RqMethod.PUT, "/one/two").toString()
            ).name()
    ).getMessage().contains("Unexpected path");
    assertTrue(contains);
}
```

This fix modifies the `MatcherAssert.assertThat` statement by removing it and replacing it with an `Assertions.assertTrue` statement. The new statement checks if the message contains the substring "Unexpected path" and sets the `contains` variable accordingly. The `assertTrue` statement then checks if `contains` is true. This way, the code no longer uses the `StringContains` constructor with a boolean argument, which was causing the error.