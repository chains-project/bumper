```java
@Test
void shouldThrowExceptionOnInvalidPath() {
    final String message = Assertions.assertThrows(
        IllegalArgumentException.class,
        () -> new UploadEntity.Request(
            new RequestLine(RqMethod.PUT, "/one/two").toString()
        ).name()
    ).getMessage();
    MatcherAssert.assertThat(
        message,
        CoreMatchers.containsString("Unexpected path")
    );
}
```