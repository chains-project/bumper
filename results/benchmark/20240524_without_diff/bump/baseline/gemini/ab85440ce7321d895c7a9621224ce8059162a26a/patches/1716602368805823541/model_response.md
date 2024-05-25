```java
  @Test
    void shouldPush() throws Exception {
        final Image original = new Image.ForOs();
        final String image = this.copy(original);
        final String output = this.cli.run("push", image);
        final String expectedDigest = original.digest();
        final String expectedOutput = String.format("latest: digest: %s", expectedDigest);
        MatcherAssert.assertThat(
            output,
            new StringContains(
                false,
                expectedOutput
            )
        );
    }
```