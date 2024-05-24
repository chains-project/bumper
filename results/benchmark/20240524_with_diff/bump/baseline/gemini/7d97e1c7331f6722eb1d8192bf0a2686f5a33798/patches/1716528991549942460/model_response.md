```java
import com.jcabi.aspects.Tv;
import com.jcabi.aspects.TvChannel;
import com.jcabi.aspects.TvProgram;

import java.util.List;

public class RegionITCase {

    @Override
    public void testRegion() throws Exception {
        Tv tv = new Tv();
        List<TvChannel> channels = tv.getChannels();
        for (TvChannel channel : channels) {
            List<TvProgram> programs = channel.getPrograms();
            for (TvProgram program : programs) {
                System.out.println(program.getName());
            }
        }
    }
}
```