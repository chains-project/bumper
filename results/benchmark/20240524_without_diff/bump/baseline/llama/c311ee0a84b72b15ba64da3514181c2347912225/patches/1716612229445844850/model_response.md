```java
@Test
void shouldThrowExceptionOnInvalidPath() {
    String expectedMessage = "Unexpected path";
    Throwable throwable = Assertions.assertThrows(
        IllegalArgumentException.class,
        () -> new UploadEntity.Request(
            new RequestLine(RqMethod.PUT, "/one/two").toString()
        ).name()
    );
    MatcherAssert.assertThat(throwable.getMessage(), Matchers.containsString(expectedMessage));
}
```