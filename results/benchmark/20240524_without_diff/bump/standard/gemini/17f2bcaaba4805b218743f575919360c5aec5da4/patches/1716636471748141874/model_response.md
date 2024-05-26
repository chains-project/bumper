```java
import processing.core.PShape;

public class PGS_MorphologyGroupShapeTests {

  public void testDilate() {
    PShape shape = new PShape();
    shape.beginShape();
    shape.vertex(0, 0);
    shape.vertex(10, 0);
    shape.vertex(10, 10);
    shape.vertex(0, 10);
    shape.endShape();

    PShape dilatedShape = PGS.dilate(shape, 5);

    // Assert that the dilated shape is as expected.
  }

  public void testErode() {
    PShape shape = new PShape();
    shape.beginShape();
    shape.vertex(0, 0);
    shape.vertex(10, 0);
    shape.vertex(10, 10);
    shape.vertex(0, 10);
    shape.endShape();

    PShape erodedShape = PGS.erode(shape, 5);

    // Assert that the eroded shape is as expected.
  }

  public void testOpen() {
    PShape shape = new PShape();
    shape.beginShape();
    shape.vertex(0, 0);
    shape.vertex(10, 0);
    shape.vertex(10, 10);
    shape.vertex(0, 10);
    shape.endShape();

    PShape openedShape = PGS.open(shape, 5);

    // Assert that the opened shape is as expected.
  }

  public void testClose() {
    PShape shape = new PShape();
    shape.beginShape();
    shape.vertex(0, 0);
    shape.vertex(10, 0);
    shape.vertex(10, 10);
    shape.vertex(0, 10);
    shape.endShape();

    PShape closedShape = PGS.close(shape, 5);

    // Assert that the closed shape is as expected.
  }

  public void testOutline() {
    PShape shape = new PShape();
    shape.beginShape();
    shape.vertex(0, 0);
    shape.vertex(10, 0);
    shape.vertex(10, 10);
    shape.vertex(0, 10);
    shape.endShape();

    PShape outlineShape = PGS.outline(shape);

    // Assert that the outline shape is as expected.
  }

  public void testSimplify() {
    PShape shape = new PShape();
    shape.beginShape();
    shape.vertex(0, 0);
    shape.vertex(10, 0);
    shape.vertex(10, 10);
    shape.vertex(0, 10);
    shape.endShape();

    PShape simplifiedShape = PGS.simplify(shape, 5);

    // Assert that the simplified shape is as expected.
  }

  public void testTriangulate() {
    PShape shape = new PShape();
    shape.beginShape();
    shape.vertex(0, 0);
    shape.vertex(10, 0);
    shape.vertex(10, 10);
    shape.vertex(0, 10);
    shape.endShape();

    PShape triangulatedShape = PGS.triangulate(shape);

    // Assert that the triangulated shape is as expected.
  }

  public void testConvexHull() {
    PShape shape = new PShape();
    shape.beginShape();
    shape.vertex(0, 0);
    shape.vertex(10, 0);
    shape.vertex(10, 10);
    shape.vertex(0, 10);
    shape.endShape();

    PShape convexHullShape = PGS.convexHull(shape);

    // Assert that the convex hull shape is as expected.
  }

  public void testAlphaMax() {
    PShape shape = new PShape();
    shape.beginShape();
    shape.vertex(0, 0);
    shape.vertex(10, 0);
    shape.vertex(10, 10);
    shape.vertex(0, 10);
    shape.endShape();

    PShape alphaMaxShape = PGS.alphaMax(shape);

    // Assert that the alpha max shape is as expected.
  }

  public void testAlphaMin() {
    PShape shape = new PShape();
    shape.beginShape();
    shape.vertex(0, 0);
    shape.vertex(10, 0);
    shape.vertex(10, 10);
    shape.vertex(0, 10);
    shape.endShape();

    PShape alphaMinShape = PGS.alphaMin(shape);

    // Assert that the alpha min shape is as expected.
  }

  public void testAlphaAverage() {
    PShape shape = new PShape();
    shape.beginShape();
    shape.vertex(0, 0);
    shape.vertex(10, 0);
    shape.vertex(10, 10);
    shape.vertex(0, 10);
    shape.endShape();

    PShape alphaAverageShape = PGS.alphaAverage(shape);

    // Assert that the alpha average shape is as expected.
  }

  public void testAlphaInvert() {
    PShape shape = new PShape();
    shape.beginShape();
    shape.vertex(0, 0);
    shape.vertex(10, 0);
    shape.vertex(10, 10);
    shape.vertex(0, 10);
    shape.endShape();

    PShape alphaInvertShape = PGS.alphaInvert(shape);

    // Assert that the alpha invert shape is as expected.
  }

  public void testAlphaThreshold() {
    PShape shape = new PShape();
    shape.beginShape();
    shape.vertex(0, 0);
    shape.vertex(10, 0);
    shape.vertex(10, 10);
    shape.vertex(0, 10);
    shape.endShape();

    PShape alphaThresholdShape = PGS.alphaThreshold(shape, 127);

    // Assert that the alpha threshold shape is as expected.
  }

  public void testAlphaMask() {
    PShape shape = new PShape();
    shape.beginShape();
    shape.vertex(0, 0);
    shape.vertex(10, 0);
    shape.vertex(10, 10);
    shape.vertex(0, 10);
    shape.endShape();

    PShape maskShape = new PShape();
    maskShape.beginShape();
    maskShape.vertex(0, 0);
    maskShape.vertex(10, 0);
    maskShape.vertex(10, 10);
    maskShape.vertex(0, 10);
    maskShape.endShape();

    PShape alphaMaskShape = PGS.alphaMask(shape, maskShape);

    // Assert that the alpha mask shape is as expected.
  }

  public void testAlphaReplace() {
    PShape shape = new PShape();
    shape.beginShape();
    shape.vertex(0, 0);
    shape.vertex(10, 0);
    shape.vertex(10, 10);
    shape.vertex(0, 10);
    shape.endShape();

    PShape alphaReplaceShape = PGS.alphaReplace(shape, 127);

    // Assert that the alpha replace shape is as expected.
  }

  public void testAlphaAdd() {
    PShape shape = new PShape();
    shape.beginShape();
    shape.vertex(0, 0);
    shape.vertex(10, 0);
    shape.vertex(10, 10);
    shape.vertex(0, 10);
    shape.endShape();

    PShape alphaAddShape = PGS.alphaAdd(shape, 127);

    // Assert that the alpha add shape is as expected.
  }

  public void testAlphaSubtract() {
    PShape shape = new PShape();
    shape.beginShape();
    shape.vertex(0, 0);
    shape.vertex(10, 0);
    shape.vertex(10, 10);
    shape.vertex(0, 10);
    shape.endShape();

    PShape alphaSubtractShape = PGS.alphaSubtract(shape, 127);

    // Assert that the alpha subtract shape is as expected.
  }

  public void testAlphaMultiply() {
    PShape shape = new PShape();
    shape.beginShape();
    shape.vertex(0, 0);
    shape.vertex(10, 0);
    shape.vertex(10, 10);
    shape.vertex(0, 10);
    shape.endShape();

    PShape alphaMultiplyShape = PGS.alphaMultiply(shape, 127);

    // Assert that the alpha multiply shape is as expected.
  }

  public void testAlphaDivide() {
    PShape shape = new PShape();
    shape.beginShape();
    shape.vertex(0, 0);
    shape.vertex(10, 0);
    shape.vertex(10, 10);
    shape.vertex(0, 10);
    shape.endShape();

    PShape alphaDivideShape = PGS.alphaDivide(shape, 127);

    // Assert that the alpha divide shape is as expected.
  }

  public void testAlphaMod() {
    PShape shape = new PShape();
    shape.beginShape();
    shape.vertex(0, 0);
    shape.vertex(10, 0);
    shape.vertex(10, 10);
    shape.vertex(0, 10);
    shape.endShape();

    PShape alphaModShape = PGS.alphaMod(shape, 127);

    // Assert that the alpha mod shape is as expected.
  }

  public void testAlphaSin() {
    PShape shape = new PShape();
    shape.beginShape();
    shape.vertex(0, 0);
    shape.vertex(10, 0);
    shape.vertex(10, 10);
    shape.vertex(0, 10);
    shape.endShape();

    PShape alphaSinShape = PGS.alphaSin(shape);

    // Assert that the alpha sin shape is as expected.
  }

  public void testAlphaCos() {
    PShape shape = new PShape();
    shape.beginShape();
    shape.vertex(0, 0);
    shape.vertex(10, 0);
    shape.vertex(10, 10);
    shape.vertex(0, 10);
    shape.endShape();

    PShape alphaCosShape = PGS.alphaCos(shape);

    // Assert that the alpha cos shape is as expected.
  }

  public void testAlphaTan() {
    PShape shape = new PShape();
    shape.beginShape();
    shape.vertex(0, 0);
    shape.vertex(10, 0);
    shape.vertex(10, 10);
    shape.vertex(0, 10);
    shape.endShape();

    PShape alphaTanShape = PGS.alphaTan(shape);

    // Assert that the alpha tan shape is as expected.
  }

  public void testAlphaAtan() {
    PShape shape = new PShape();
    shape.beginShape();
    shape.vertex(0, 0);
    shape.vertex(10, 0);
    shape.vertex(10, 10);
    shape.vertex(0, 10);
    shape.endShape();

    PShape alphaAtanShape = PGS.alphaAtan(shape);

    // Assert that the alpha atan shape is as expected.
  }

  public void testAlphaExp() {
    PShape shape = new PShape();
    shape.beginShape();
    shape.vertex(0, 0);
    shape.vertex(10, 0);
    shape.vertex(10, 10);
    shape.vertex(0, 10);
    shape.endShape();

    PShape alphaExpShape = PGS.alphaExp(shape);

    // Assert that the alpha exp shape is as expected.
  }

  public void testAlphaLog() {
    PShape shape = new PShape();
    shape.beginShape();
    shape.vertex(0, 0);
    shape.vertex(10, 0);
    shape.vertex(10, 10);
    shape.vertex(0, 10);
    shape.endShape();

    PShape alphaLogShape = PGS.alphaLog(shape);

    // Assert that the alpha log shape is as expected.
  }

  public void testAlphaPow() {
    PShape shape = new PShape();
    shape.beginShape();
    shape.vertex(0, 0);
    shape.vertex(10, 0);
    shape.vertex(10, 10);
    shape.vertex(0, 10);
    shape.endShape();

    PShape alphaPowShape = PGS.alphaPow(shape, 2);

    // Assert that the alpha pow shape is as expected.
  }

  public void testAlphaSqrt() {
    PShape shape = new PShape();
    shape.beginShape();
    shape.vertex(0, 0);
    shape.vertex(10, 0);
    shape.vertex(10, 10);
    shape.vertex(0, 10);
    shape.endShape();

    PShape alphaSqrtShape = PGS.alphaSqrt(shape);

    // Assert that the alpha sqrt shape is as expected.
  }

  public void testAlphaAbs() {
    PShape shape = new PShape();
    shape.beginShape();
    shape.vertex(0, 0);
    shape.vertex(10, 0);
    shape.vertex(10, 10);
    shape.vertex(0, 10);
    shape.endShape();

    PShape alphaAbsShape = PGS.alphaAbs(shape);

    // Assert that the alpha abs shape is as expected.
  }

  public void testAlphaFloor() {
    PShape shape = new PShape();
    shape.beginShape();
    shape.vertex(0, 0);
    shape.vertex(10, 0);
    shape.vertex(10, 10);
    shape.vertex(0, 10);
    shape.endShape();

    PShape alphaFloorShape = PGS.alphaFloor(shape);

    // Assert that the alpha floor shape is as expected.
  }

  public void testAlphaCeil() {
    PShape shape = new PShape();
    shape.beginShape();
    shape.vertex(0, 0);
    shape.vertex(10, 0);
    shape.vertex(10, 10);
    shape.vertex(0, 10);
    shape.endShape();

    PShape alphaCeilShape = PGS.alphaCeil(shape);

    // Assert that the alpha ceil shape is as expected.
  }

  public void testAlphaRound() {
    PShape shape = new PShape();
    shape.beginShape();
    shape.vertex(0, 0);
    shape.vertex(10, 0);
    shape.vertex(10, 10);
    shape.vertex(0, 10);
    shape.endShape();

    PShape alphaRoundShape = PGS.alphaRound(shape);

    // Assert that the alpha round shape is as expected.
  }

  public void testAlphaMap() {
    PShape shape = new PShape();
    shape.beginShape();
    shape.vertex(0, 0);
    shape.vertex(10, 0);
    shape.vertex(10, 10);
    shape.vertex(0, 10);
    shape.endShape();

    PShape alphaMapShape = PGS.alphaMap(shape, 0, 255, 127, 255);

    // Assert that the alpha map shape is as expected.
  }

  public void testAlphaNormalize() {
    PShape shape = new PShape();
    shape.beginShape();
    shape.vertex(0, 0);
    shape.vertex(10, 0);
    shape.vertex(10, 10);
    shape.vertex(0, 10);
    shape.endShape();

    PShape alphaNormalizeShape = PGS.alphaNormalize(shape);

    // Assert that the alpha normalize shape is as expected.
  }

  public void testAlphaDither() {
    PShape shape = new PShape();
    shape.beginShape();
    shape.vertex(0, 0);
    shape.vertex(10, 0);
    shape.vertex(10, 10);
    shape.vertex(0, 10);
    shape.endShape();

    PShape alphaDitherShape = PGS.alphaDither(shape, 2);

    // Assert that the alpha dither shape is as expected.
  }

  public void testAlphaPosterize() {
    PShape shape = new PShape();
    shape.beginShape();
    shape.vertex(0, 0);
    shape.vertex(10, 0);
    shape.vertex(10, 10);
    shape.vertex(0, 10);
    shape.endShape();

    PShape alphaPosterizeShape = PGS.alphaPosterize(shape, 2);

    // Assert that the alpha posterize shape is as expected.
  }

  public void testAlphaThresholdMap() {
    PShape shape = new PShape();
    shape.beginShape();
    shape.vertex(0, 0);
    shape.vertex(10, 0);
    shape.vertex(10, 10);
    shape.vertex(0, 10);
    shape.endShape();

    PShape alphaThresholdMapShape = PGS.alphaThresholdMap(shape, 127, 255, 0);

    // Assert that the alpha threshold map shape is as expected.
  }

  public void testAlphaAddNoise() {
    PShape shape = new PShape();
    shape.beginShape();
    shape.vertex(0, 0);
    shape.vertex(10, 0);
    shape.vertex(10, 10);
    shape.vertex(0, 10);
    shape.endShape();

    PShape alphaAddNoiseShape = PGS.alphaAddNoise(shape, 0.1f);

    // Assert that the alpha add noise shape is as expected.
  }

  public void testAlphaSubtractNoise() {
    PShape shape = new PShape();
    shape.beginShape();
    shape.vertex(0, 0);
    shape.vertex(10, 0);
    shape.vertex(10, 10);
    shape.vertex(0, 10);
    shape.endShape();

    PShape alphaSubtractNoiseShape = PGS.alphaSubtractNoise(shape, 0.1f);

    // Assert that the alpha subtract noise shape is as expected.
  }

  public void testAlphaMultiplyNoise() {
    PShape shape = new PShape();
    shape.beginShape();
    shape.vertex(0, 0);
    shape.vertex(10, 0);
    shape.vertex(10, 10);
    shape.vertex(0, 10);
    shape.endShape();

    PShape alphaMultiplyNoiseShape = PGS.alphaMultiplyNoise(shape, 0.1f);

    // Assert that the alpha multiply noise shape is as expected.
  }

  public void testAlphaDivideNoise() {
    PShape shape = new PShape();
    shape.beginShape();
    shape.vertex(0, 0);
    shape.vertex(10, 0);
    shape.vertex(10, 10);
    shape.vertex(0, 10);
    shape.endShape();

    PShape alphaDivideNoiseShape = PGS.alphaDivideNoise(shape, 0.1f);

    // Assert that the alpha divide noise shape is as expected.
  }

  public void testAlphaSmooth() {
    PShape shape = new PShape();
    shape.beginShape();
    shape.vertex(0, 0);
    shape.vertex(10, 0);
    shape.vertex(10, 10);
    shape.vertex(0, 10);
    shape.endShape();

    PShape alphaSmoothShape = PGS.alphaSmooth(shape, 0.1f);

    // Assert that the alpha smooth shape is as expected.
  }

  public void testAlphaBlur() {
    PShape shape = new PShape();
    shape.beginShape();
    shape.vertex(0, 0);
    shape.vertex(10, 0);
    shape.vertex(10, 10);
    shape.vertex(0, 10);
    shape.endShape();

    PShape alphaBlurShape = PGS.alphaBlur(shape, 0.1f);

    // Assert that the alpha blur shape is as expected.
  }

  public void testAlphaGaussianBlur() {
    PShape shape = new PShape();
    shape.beginShape();
    shape.vertex(0, 0);
    shape.vertex(10, 0);
    shape.vertex(10, 10);
    shape.vertex(0, 10);
    shape.endShape();

    PShape alphaGaussianBlurShape = PGS.alphaGaussianBlur(shape, 0.1f);

    // Assert that the alpha gaussian blur shape is as expected.
  }

  public void testAlphaMedianFilter() {
    PShape shape = new PShape();
    shape.beginShape();
    shape.vertex(0, 0);
    shape.vertex(10, 0);
    shape.vertex(10, 10);
    shape.vertex(0, 10);
    shape.endShape();

    PShape alphaMedianFilterShape = PGS.alphaMedianFilter(shape, 3);

    // Assert that the alpha median filter shape is as expected.
  }

  public void testAlphaModeFilter() {
    PShape shape = new PShape();
    shape.beginShape();
    shape.vertex(0, 0);
    shape.vertex(10, 0);
    shape.vertex(10, 10);
    shape.vertex(0, 10);
    shape.endShape();

    PShape alphaModeFilterShape = PGS.alphaModeFilter(shape, 3);

    // Assert that the alpha mode filter shape is as expected.
  }

  public void testAlphaErode() {
    PShape shape = new PShape();
    shape.beginShape();
    shape.vertex(0, 0);
    shape.vertex(10, 0);
    shape.vertex(10, 10);
    shape.vertex(0, 10);
    shape.endShape();

    PShape alphaErodeShape = PGS.alphaErode(shape, 3);

    // Assert that the alpha erode shape is as expected.
  }

  public void testAlphaDilate() {
    PShape shape = new PShape();
    shape.beginShape();
    shape.vertex(0, 0);
    shape.vertex(10, 0);
    shape.vertex(10, 10);
    shape.vertex(0, 10);
    shape.endShape();

    PShape alphaDilateShape = PGS.alphaDilate(shape, 3);

    // Assert that the alpha dilate shape is as expected.
  }

  public void testAlphaGradient() {
    PShape shape = new PShape();
    shape.beginShape();
    shape.vertex(0, 0);
    shape.vertex(10, 0);
    shape.vertex(10, 10);
    shape.vertex(0, 10);
    shape.endShape();

    PShape alphaGradientShape = PGS.alphaGradient(shape, 0, 255);

    // Assert that the alpha gradient shape is as expected.
  }

  public void testAlphaSobel() {
    PShape shape = new PShape();
    shape.beginShape();
    shape.vertex(0, 0);
    shape.vertex(10, 0);
    shape.vertex(10, 10);
    shape.vertex(0, 10);
    shape.endShape();

    PShape alphaSobelShape = PGS.alphaSobel(shape);

    // Assert that the alpha sobel shape is as expected.
  }

  public void testAlphaPrewitt() {
    PShape shape = new PShape();
    shape.beginShape();
    shape.vertex(0, 0);
    shape.vertex(10, 0);
    shape.vertex(10, 10);
    shape.vertex(0, 10);
    shape.endShape();

    PShape alphaPrewittShape = PGS.alphaPrewitt(shape);

    // Assert that the alpha prewitt shape is as expected.
  }

  public void testAlphaLaplacian() {
    PShape shape = new PShape();
    shape.beginShape();
    shape.vertex(0, 0);
    shape.vertex(10, 0);
    shape.vertex(10, 10);
    shape.vertex(0, 10);
    shape.endShape();

    PShape alphaLaplacianShape = PGS.alphaLaplacian(shape);

    // Assert that the alpha laplacian shape is as expected.
  }

  public void testAlphaCanny() {
    PShape shape = new PShape();
    shape.beginShape();
    shape.vertex(0, 0);
    shape.vertex(10, 0);
    shape.vertex(10, 10);
    shape.vertex(0, 10);
    shape.endShape();

    PShape alphaCannyShape = PGS.alphaCanny(shape, 10, 50);

    // Assert that the alpha canny shape is as expected.
  }
}
```