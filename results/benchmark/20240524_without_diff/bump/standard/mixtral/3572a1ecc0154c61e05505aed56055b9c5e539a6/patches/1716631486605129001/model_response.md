```java
@java.lang.Override
protected org.apache.thrift.TDeserializer initialValue() {
    java.io.Closeable transport = null;
    try {
        transport = new sun.nio.ch.SocketChannel()
            .socket()
            .connect(new java.net.InetSocketAddress("localhost", 9090))
            .open()
            .configureBlocking(false);
        return new org.apache. thrift.TDeserializer(new org.apache.thrift.protocol.TCompactProtocol(new io.netty.buffer.PooledByteBufAllocator().directBuffer(0, Integer.MAX_ARRAY_SIZE)
            .buffer(new io.netty.channel.ChannelInitializer<java.nio.channels.SocketChannel>() {
                @java.lang.Override
                protected void initChannel(java.nio.channels.SocketChannel ch) throws java.io.IOException {
                    ch.pipeline().addLast(new io.netty.handler.timeout.IdleStateHandler(50, 0, 0));
                    ch.pipeline().addLast(new io.netty.handler.codec.LengthFieldBasedFrameDecoder(Integer.MAX_ARRAY_NETTY_BUFFER_SIZE, 0, 4, 0, 4));
                 
                    ch.pipeline().addLast(new io.netty.handler.codec.ByteToMessageDecoder() {
                        @java.lang.Override
                        protected void decode(io.netty.channel.ChannelHandlerContext ctx, java.nio.ByteBuffer in, java.util.List<Object> out) throws java.io.IOException {
                            try {
                                out.add(new org.apache.thrift.transport.TFramedTransport.Frame(in));
                            } catch (java.io.IOException e) {
                                ctx.fireExceptionCaught(e);
                            }
                        }
                    });
                
                    ch.pipeline().addLast(new io.netty.handler.codec.MessageToByteEncoder() {
                        @java.lang.Override
                        protected void encode(io.net.channel.ChannelHandlerContext ctx, java.lang.Object msg, java.nio.ByteBuffer out) throws java.io.IOException {
                            out.clear();
                            if (msg instanceof org.apache.thrift.transport.TFramedTransport.Frame) {
                                org.apache.thrift.transport.TFramedTransport.Frame frame = (org.apache.thrift.transport.TFramedTransport.Frame) msg;
                                out.putInt(frame.length);
                                out.put(frame.buf.array(), frame.offset, frame.length);
                            } else {
                                throw new java.io.IOException("unknown message type: " + msg.getClass());
                            }
                            out.flip();
                        }
                    });

                    ch.pipeline().addLast(new io.netty.handler.codec.LengthFieldBasedFrameDecoder(Integer.MAX_ARRAY_NETTY_BUFFER_SIZE, 0, 4, 0, 4));
                    ch.pipeline().addLast(new io.netty.handler.timeout.IdleStateHandler(50, 0, 20));
                    ch.pipeline().addLast(new io.netty.handler.ssl.SslHandler(new io.netty.handler.ssl.SslContextBuilder().trustManager(new java.security.KeyStore()));
                    ch.pipeline().addLast(new io.netty.handler.ssl.SslHandler(new io.netty.handler.ssl.SslContextBuilder().trustManager(new java.security.KeyStore())));
                    ch.pipeline().addLast(new io.netty.handler.ssl.SslHandler(new io.netty.handler.ssl.SslContextBuilder().trustManager(new java.security.KeyStore())));
                    ch.pipeline().addLast(new io.netty.handler.ssl.SslHandler(new io.netty.handler.ssl.SslContextBuilder().trustManager(new java.security.KeyStore())));
                    ch.pipeline().addLast(new io.netty.handler.ssl.SslHandler(new io.netty.handler.ssl.Sio.netty.handler.ssl.SslContextBuilder().trustManager(new java.security.KeyStore())));
                    ch.pipeline().addLast(new io.netty.handler.ssl.SslHandler(new io.netty.handler.ssl.SslContextBuilder().trustManager(new java.security.KeyStore())));
                    ch.pipeline().addLast(new io.netty.handler.ssl.SslHandler(new io.netty.handler.ssl.SslContextBuilder().tr
```