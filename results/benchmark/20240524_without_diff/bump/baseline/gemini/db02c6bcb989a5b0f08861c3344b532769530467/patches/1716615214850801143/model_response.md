```java
 @Test
    public void shouldPush() throws Exception {
        final Image original = new Image.ForOs();
        final String image = this.copy(original);
        final String output = this.cli.run("push", image);
        String expectedDigest = original.digest().toString();
        MatcherAssert.assertThat(
                output,
                new StringContains(
                        false,
                        String.format("latest: digest: %s", expectedDigest)
                )
        );
    }
```