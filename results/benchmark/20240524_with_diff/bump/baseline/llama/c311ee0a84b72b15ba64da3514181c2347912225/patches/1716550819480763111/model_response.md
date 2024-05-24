```java
@Test
void shouldThrowExceptionOnInvalidPath() {
    Throwable throwable = Assertions.assertThrows(
        IllegalArgumentException.class,
        () -> new UploadEntity.Request(
            new RequestLine(RqMethod.PUT, "/one/two").toString()
        ).name()
    );
    MatcherAssert.assertThat(throwable.getMessage(), CoreMatchers.containsString("Unexpected path"));
}
```