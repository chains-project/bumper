```java
  import com.jcabi.aspects.Tv;
  import com.jcabi.aspects.TvSeries;

  public class RegionITCase {

    private final TvSeries series = new TvSeries(new Tv(new SimpleDb(this.region())));

    @Test
    @Override
    public void testCreate() throws Exception {
      final String name = "Breaking Bad";
      final Tv tv = this.series.get(name);
      Assert.assertNotNull(tv);
      Assert.assertEquals(name, tv.name());
    }

    @Test
    @Override
    public void testUpdate() throws Exception {
      final String name = "Breaking Bad";
      final Tv tv = this.series.get(name);
      Assert.assertNotNull(tv);
      tv.name("Better Call Saul");
      Assert.assertEquals("Better Call Saul", tv.name());
    }

    @Test
    @Override
    public void testDelete() throws Exception {
      final String name = "Breaking Bad";
      final Tv tv = this.series.get(name);
      Assert.assertNotNull(tv);
      tv.delete();
      Assert.assertNull(this.series.get(name));
    }

    private SimpleDb region() {
      return new SimpleDb(this.region());
    }
  }
```