```java
@Test
void shouldThrowExceptionOnInvalidPath() {
    String errorMsg = Assertions.assertThrows(
        IllegalArgumentException.class,
        () -> new UploadEntity.Request(
            new RequestLine(RqMethod.PUT, "/one/two").toString()
        ).name()
    ).getMessage();
    MatcherAssert.assertThat(errorMsg, CoreMatchers.containsString("Unexpected path"));
}
```