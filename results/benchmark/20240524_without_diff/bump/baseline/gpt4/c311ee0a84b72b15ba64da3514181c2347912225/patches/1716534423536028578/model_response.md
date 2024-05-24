```java
@Test
void shouldThrowExceptionOnInvalidPath() {
    final String msg = Assertions.assertThrows(
        IllegalArgumentException.class,
        () -> new UploadEntity.Request(
            new RequestLine(RqMethod.PUT, "/one/two").toString()
        ).name()
    ).getMessage();
    MatcherAssert.assertThat(
        msg,
        CoreMatchers.containsString("Unexpected path")
    );
}
```