```java
@Test
void shouldThrowExceptionOnInvalidPath() {
    Throwable exception = Assertions.assertThrows(
        IllegalArgumentException.class,
        () -> new UploadEntity.Request(
            new RequestLine(RqMethod.PUT, "/one/two").toString()
        ).name()
    );
    String message = exception.getMessage();
    assertThat(message, CoreMatchers.containsString("Unexpected path"));
}
```