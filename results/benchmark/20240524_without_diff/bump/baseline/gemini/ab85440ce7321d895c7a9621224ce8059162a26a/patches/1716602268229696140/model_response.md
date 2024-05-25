```java
  @Test
    public void shouldPush() throws Exception {
        final Image original = new Image.ForOs();
        final String image = this.copy(original);
        final String output = this.cli.run("push", image);
        MatcherAssert.assertThat(
            output,
            new StringContains(
                false,
                new StringBuilder().append("latest: digest: ").append(original.digest()).toString()
            )
        );
    }
```