```java
  @Test
    public void shouldThrowExceptionOnInvalidPath() {
        MatcherAssert.assertThat(
            Assertions.assertThrows(
                IllegalArgumentException.class,
                () -> new UploadEntity.Request(
                    new RequestLine(RqMethod.PUT, "/one/two").toString()
                ).name()
            ).getMessage(),
            containsString("Unexpected path")
        );
    }
```