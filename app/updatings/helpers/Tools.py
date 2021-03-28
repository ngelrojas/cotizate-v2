from core.upload import Upload
from core.campaing import CampaingHeader


class Tools:
    def saving_images(self, request, image_url):
        """saving url of image"""
        camp_id = CampaingHeader.objects.get(id=request.data.get("camp_id"))
        created = Upload.objects.get_or_create(
            name=image_url,
            campaings=camp_id,
        )
        return created
