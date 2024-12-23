```java
import org.apache.maven.doxia.decoration.model.List;
import org.apache.maven.doxia.sink.Sink;
import org.apache.maven.doxia.sink.SinkEventAttributes;
import org.apache.maven.doxia.sink.SinkEventElement;

import java.util.Map;

/**
 * Renders a list.
 *
 * @author <a href="mailto:vincent.siveton@gmail.com">Vincent Siveton</a>
 * @since 1.0
 */
public class ListSinkRenderer
{
    /**
     * Render the list.
     *
     * @param list the list to render
     * @param sink the sink
     * @param context the rendering context
     * @throws org.apache.maven.doxia.sink.SinkException if an error occurs while rendering
     */
    public void render( List list, Sink sink, RenderingContext context )
        throws org.apache.maven.doxia.sink.SinkException
    {
        if ( list == null )
        {
            return;
        }

        Map attributes = list.getAttributes();
        if ( attributes != null && !attributes.isEmpty() )
        {
            sink.sinkEvent( SinkEventElement.START_ELEMENT, "ul", attributes );
        }
        else
        {
            sink.sinkEvent( SinkEventElement.START_ELEMENT, "ul" );
        }

        List.Type type = list.getType();
        if ( type != null )
        {
            if ( type.equals( List.Type.BULLETED ) )
            {
                sink.sinkEvent( SinkEventElement.START_ELEMENT, "li", SinkEventAttributes.LIST_ITEM_TYPE_BULLET );
            }
            else if ( type.equals( List.Type.NUMBERED ) )
            {
                sink.sinkEvent( SinkEventElement.START_ELEMENT, "li", SinkEventAttributes.LIST_ITEM_TYPE_NUMBER );
            }
        }
        else
        {
            sink.sinkEvent( SinkEventElement.START_ELEMENT, "li" );
        }

        if ( list.getMarker() != null )
        {
            sink.sinkEvent( SinkEventElement.START_ELEMENT, "span", SinkEventAttributes.LIST_MARKER );
            sink.text( list.getMarker() );
            sink.sinkEvent( SinkEventElement.END_ELEMENT, "span" );
        }

        if ( list.getContent() != null )
        {
            sink.text( list.getContent() );
        }

        sink.sinkEvent( SinkEventElement.END_ELEMENT, "li" );

        if ( attributes != null && !attributes.isEmpty() )
        {
            sink.sinkEvent( SinkEventElement.END_ELEMENT, "ul", attributes );
        }
        else
        {
            sink.sinkEvent( SinkEventElement.END_ELEMENT, "ul" );
        }
    }
}
```