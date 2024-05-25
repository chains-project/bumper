```java
import org.apache.thrift.transport.TFastFramedTransport;

import java.io.IOException;
import java.nio.ByteBuffer;
import java.nio.charset.StandardCharsets;
import java.util.Base64;

public class AppenderUtils {

    public static byte[] encodeBase64(byte[] data) {
        return Base64.getEncoder().encode(data);
    }

    public static byte[] decodeBase64(byte[] data) {
        return Base64.getDecoder().decode(data);
    }

    public static byte[] encodeBase64(String data) {
        return encodeBase64(data.getBytes(StandardCharsets.UTF_8));
    }

    public static String decodeBase64(String data) {
        return new String(decodeBase64(data.getBytes(StandardCharsets.UTF_8)), StandardCharsets.UTF_8);
    }

    public static byte[] encodeBase64(ByteBuffer data) {
        return encodeBase64(data.array(), data.position(), data.remaining());
    }

    public static byte[] encodeBase64(byte[] data, int offset, int length) {
        return Base64.getEncoder().encode(data, offset, length);
    }

    public static ByteBuffer decodeBase64(ByteBuffer data) {
        return ByteBuffer.wrap(decodeBase64(data.array(), data.position(), data.remaining()));
    }

    public static ByteBuffer decodeBase64(byte[] data, int offset, int length) {
        return ByteBuffer.wrap(Base64.getDecoder().decode(data, offset, length));
    }

    public static byte[] encodeUTF8(String data) {
        return data.getBytes(StandardCharsets.UTF_8);
    }

    public static String decodeUTF8(byte[] data) {
        return new String(data, StandardCharsets.UTF_8);
    }

    public static byte[] encodeUTF8(ByteBuffer data) {
        return encodeUTF8(data.array(), data.position(), data.remaining());
    }

    public static byte[] encodeUTF8(byte[] data, int offset, int length) {
        return data.toString().getBytes(StandardCharsets.UTF_8);
    }

    public static ByteBuffer decodeUTF8(ByteBuffer data) {
        return ByteBuffer.wrap(decodeUTF8(data.array(), data.position(), data.remaining()));
    }

    public static ByteBuffer decodeUTF8(byte[] data, int offset, int length) {
        return ByteBuffer.wrap(data.toString().getBytes(StandardCharsets.UTF_8));
    }

    public static byte[] encodeUTF16(String data) {
        return data.getBytes(StandardCharsets.UTF_16);
    }

    public static String decodeUTF16(byte[] data) {
        return new String(data, StandardCharsets.UTF_16);
    }

    public static byte[] encodeUTF16(ByteBuffer data) {
        return encodeUTF16(data.array(), data.position(), data.remaining());
    }

    public static byte[] encodeUTF16(byte[] data, int offset, int length) {
        return data.toString().getBytes(StandardCharsets.UTF_16);
    }

    public static ByteBuffer decodeUTF16(ByteBuffer data) {
        return ByteBuffer.wrap(decodeUTF16(data.array(), data.position(), data.remaining()));
    }

    public static ByteBuffer decodeUTF16(byte[] data, int offset, int length) {
        return ByteBuffer.wrap(data.toString().getBytes(StandardCharsets.UTF_16));
    }

    public static byte[] encodeISO88591(String data) {
        return data.getBytes(StandardCharsets.ISO_8859_1);
    }

    public static String decodeISO88591(byte[] data) {
        return new String(data, StandardCharsets.ISO_8859_1);
    }

    public static byte[] encodeISO88591(ByteBuffer data) {
        return encodeISO88591(data.array(), data.position(), data.remaining());
    }

    public static byte[] encodeISO88591(byte[] data, int offset, int length) {
        return data.toString().getBytes(StandardCharsets.ISO_8859_1);
    }

    public static ByteBuffer decodeISO88591(ByteBuffer data) {
        return ByteBuffer.wrap(decodeISO88591(data.array(), data.position(), data.remaining()));
    }

    public static ByteBuffer decodeISO88591(byte[] data, int offset, int length) {
        return ByteBuffer.wrap(data.toString().getBytes(StandardCharsets.ISO_8859_1));
    }

    public static byte[] encodeASCII(String data) {
        return data.getBytes(StandardCharsets.US_ASCII);
    }

    public static String decodeASCII(byte[] data) {
        return new String(data, StandardCharsets.US_ASCII);
    }

    public static byte[] encodeASCII(ByteBuffer data) {
        return encodeASCII(data.array(), data.position(), data.remaining());
    }

    public static byte[] encodeASCII(byte[] data, int offset, int length) {
        return data.toString().getBytes(StandardCharsets.US_ASCII);
    }

    public static ByteBuffer decodeASCII(ByteBuffer data) {
        return ByteBuffer.wrap(decodeASCII(data.array(), data.position(), data.remaining()));
    }

    public static ByteBuffer decodeASCII(byte[] data, int offset, int length) {
        return ByteBuffer.wrap(data.toString().getBytes(StandardCharsets.US_ASCII));
    }

    public static byte[] encode(String data, String charset) {
        return data.getBytes(charset);
    }

    public static String decode(byte[] data, String charset) {
        return new String(data, charset);
    }

    public static byte[] encode(ByteBuffer data, String charset) {
        return encode(data.array(), data.position(), data.remaining(), charset);
    }

    public static byte[] encode(byte[] data, int offset, int length, String charset) {
        return data.toString().getBytes(charset);
    }

    public static ByteBuffer decode(ByteBuffer data, String charset) {
        return ByteBuffer.wrap(decode(data.array(), data.position(), data.remaining(), charset));
    }

    public static ByteBuffer decode(byte[] data, int offset, int length, String charset) {
        return ByteBuffer.wrap(data.toString().getBytes(charset));
    }

    public static byte[] encode(String data, Charset charset) {
        return data.getBytes(charset);
    }

    public static String decode(byte[] data, Charset charset) {
        return new String(data, charset);
    }

    public static byte[] encode(ByteBuffer data, Charset charset) {
        return encode(data.array(), data.position(), data.remaining(), charset);
    }

    public static byte[] encode(byte[] data, int offset, int length, Charset charset) {
        return data.toString().getBytes(charset);
    }

    public static ByteBuffer decode(ByteBuffer data, Charset charset) {
        return ByteBuffer.wrap(decode(data.array(), data.position(), data.remaining(), charset));
    }

    public static ByteBuffer decode(byte[] data, int offset, int length, Charset charset) {
        return ByteBuffer.wrap(data.toString().getBytes(charset));
    }

    public static byte[] encode(String data) throws IOException {
        return encode(data, StandardCharsets.UTF_8);
    }

    public static String decode(byte[] data) throws IOException {
        return decode(data, StandardCharsets.UTF_8);
    }

    public static byte[] encode(ByteBuffer data) throws IOException {
        return encode(data, StandardCharsets.UTF_8);
    }

    public static ByteBuffer decode(ByteBuffer data) throws IOException {
        return decode(data, StandardCharsets.UTF_8);
    }

    public static byte[] encode(String data, String charset) throws IOException {
        return data.getBytes(charset);
    }

    public static String decode(byte[] data, String charset) throws IOException {
        return new String(data, charset);
    }

    public static byte[] encode(ByteBuffer data, String charset) throws IOException {
        return encode(data.array(), data.position(), data.remaining(), charset);
    }

    public static byte[] encode(byte[] data, int offset, int length, String charset) throws IOException {
        return data.toString().getBytes(charset);
    }

    public static ByteBuffer decode(ByteBuffer data, String charset) throws IOException {
        return ByteBuffer.wrap(decode(data.array(), data.position(), data.remaining(), charset));
    }

    public static ByteBuffer decode(byte[] data, int offset, int length, String charset) throws IOException {
        return ByteBuffer.wrap(data.toString().getBytes(charset));
    }

    public static byte[] encode(String data, Charset charset) throws IOException {
        return data.getBytes(charset);
    }

    public static String decode(byte[] data, Charset charset) throws IOException {
        return new String(data, charset);
    }

    public static byte[] encode(ByteBuffer data, Charset charset) throws IOException {
        return encode(data.array(), data.position(), data.remaining(), charset);
    }

    public static byte[] encode(byte[] data, int offset, int length, Charset charset) throws IOException {
        return data.toString().getBytes(charset);
    }

    public static ByteBuffer decode(ByteBuffer data, Charset charset) throws IOException {
        return ByteBuffer.wrap(decode(data.array(), data.position(), data.remaining(), charset));
    }

    public static ByteBuffer decode(byte[] data, int offset, int length, Charset charset) throws IOException {
        return ByteBuffer.wrap(data.toString().getBytes(charset));
    }
}
```