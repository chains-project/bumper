```java
import eu.europa.esig.dss.pades.CertificationPermission;
import java.util.ArrayList;
import java.util.List;
import org.apache.pdfbox.pdmodel.PDDocument;
import org.apache.pdfbox.pdmodel.interactive.digitalsignature.PDSignature;
import org.apache.pdfbox.pdmodel.interactive.digitalsignature.visible.PDVisibleSignatureConstructor;

public class Signer {

    public static void main(String[] args) throws Exception {
        // Create a new PDF document
        PDDocument document = new PDDocument();

        // Create a new signature field
        PDSignature signature = new PDSignature();

        // Add the signature field to the document
        document.addSignature(signature);

        // Create a new visible signature constructor
        PDVisibleSignatureConstructor constructor = new PDVisibleSignatureConstructor();

        // Set the signature properties
        constructor.setSignerName("John Doe");
        constructor.setSignatureLocation("London");
        constructor.setSignatureReason("I am signing this document.");

        // Create the visible signature
        constructor.createSignature(signature);

        // Add the visible signature to the document
        document.addSignature(signature);

        // Save the document
        document.save("signed.pdf");

        // Close the document
        document.close();
    }
}
```