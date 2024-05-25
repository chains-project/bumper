```java
@Test
void shouldThrowExceptionOnInvalidPath() {
    String actualMessage = Assertions.assertThrows(
        IllegalArgumentException.class,
        () -> new UploadEntity.Request(
            new RequestLine(RqMethod.PUT, "/one/two").toString()
        ).name()
    ).getMessage();
    MatcherAssert.assertThat(actualMessage, CoreMatchers.containsString("Unexpected path"));
}
```