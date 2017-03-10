#~/usr/bin/env python3

import connexion

def post_manualcontrol(articulation: str, direction: str, numsteps: int) -> str:
   return "Moving {0} {1} by {2} steps\n".format(articulation, direction, numsteps)

if __name__ == '__main__':
   app = connexion.App(__name__, 8080, specification_dir='swagger/')
   app.add_api('thor_control.yaml', arguments={'title': 'Thor Arm Control'})
   app.run()
