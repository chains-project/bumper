```java
@Test
void shouldThrowExceptionOnInvalidPath() {
    String exceptionMessage = Assertions.assertThrows(
        IllegalArgumentException.class,
        () -> new UploadEntity.Request(
            new RequestLine(RqMethod.PUT, "/one/two").toString()
        ).name()
    ).getMessage();
    MatcherAssert.assertThat(
        exceptionMessage,
        CoreMatchers.containsString("Unexpected path")
    );
}
```